/*
Dette programmet simulerer et LxL spinsystem med tilfeldig startkonfigurasjon for et invervall med temperaturer.
Variabler som må sendes med er: L Tmin Tmax dT antallMCC filnavn.
Antall Monte Carlo sykluser blir fordelt på antall parallelle prosesser.
Vi tar gjennomsnittet av forventningsverdiene over alle de parallelle prosessene, og det er dette som printes.
*/
#include <mpi.h>
#include <armadillo>
#include <cstdlib>
#include <random>
#include <iostream>
#include <iomanip>


using namespace std;
using namespace arma;

ofstream ofile;
//Funksjon som lager perodiske grensebetingelser
inline double periodic(int val,int add, int L){
  return (val+L+add)%L;
}


void init(int,mat &,double &,double &,uniform_real_distribution<double> &, mt19937_64 &);
void sweep(int,double &,double &,mat &,vec,vec,uniform_real_distribution<double> &, mt19937_64 &);
int nearsum(int, int, mat &,int);
void outputexpect(int, int ,double, vec);
double ran2(long *);

int main(int argc, char* argv[]){
  //Starter parallellisering
  int cores, core_pos;
  MPI_Init(&argc, &argv);
  MPI_Comm_size (MPI_COMM_WORLD, &cores);
  MPI_Comm_rank (MPI_COMM_WORLD, &core_pos);

  //Definerer variabler
  int maxmcc = atof(argv[5]);
  int L = atof(argv[1]);
  double Tmin = atof(argv[2]);
  double Tmax = atof(argv[3]);
  double deltaT = atof(argv[4]);
  vec DE = {8, 4, 0, -4, -8};

  //Definerer loop grenser
  int nr_inter = maxmcc/cores;
  int start_loop = core_pos*nr_inter+1;
  int end_loop = (core_pos+1)*nr_inter;
  if((core_pos == cores-1) && (end_loop < maxmcc)) end_loop = maxmcc;

  //Setter opp tilfeldige generatorer
  random_device rd;
  mt19937_64 gen(rd());
  uniform_real_distribution<double> dist(0.0,1.0);
  mat spinmat = mat(L,L);
  vec valE, expval;
  double B;

  //Åpner fil ut
  vec totalexpval = vec(5,fill::zeros);
  if (core_pos ==0){
    string fileout = argv[6];
    ofile.open(fileout);
  }

  double  TimeStart, TimeEnd, TotalTime;
  TimeStart = MPI_Wtime();

  //Loop for de forskjellige T-verdiene
  for(double T=Tmin;T<=Tmax;T+=deltaT){
    B = 1/T;
    valE = exp(-B*DE);
    expval = vec(5,fill::zeros);

    double E = 0;
    double M = 0;

    init(L,spinmat,E,M,dist,gen);

    //Loop for MC sykluser
    for(int count = start_loop;count<=end_loop;count++){
      sweep(L,E,M,spinmat,valE,DE,dist,gen);
      expval(0) += E;
      expval(1) +=E*E;
      expval(2) +=M;
      expval(3) += M*M;
      expval(4) += fabs(M);
    }
    //Legger sammen forventingsverdier til forskjellige prosesser
    for( int i =0; i < 5; i++){
      MPI_Reduce(&expval(i), &totalexpval(i), 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    }

    TimeEnd = MPI_Wtime();
    TotalTime = TimeEnd-TimeStart;
    if (core_pos==0){
      cout << "Tiden som programmet bruker for å regne ut verdiene er: " << TotalTime<<"s"<<endl;
    }
    //printer ut forventningsverdier
    if (core_pos ==0){
      outputexpect(L,maxmcc,T,totalexpval);

    }
  }
ofile.close();
MPI_Finalize();
return 0;
}

//Gjør et utvalg av mulige tilfeldige spinnendringer LxL ganger og regner ut endringer i energi og magnetisk moment
void sweep(int L,double &E,double &M,mat &spinmat,vec valE,vec DE,uniform_real_distribution<double> &dist, mt19937_64 &gen){
  int Nmax = L*L;
  for(int N=0;N<Nmax;N++){
    int x = int(floor(dist(gen)*L));
    int y = int(floor(dist(gen)*L));
    double dE = 2*spinmat(x,y)*nearsum(x,y,spinmat,L);
    uvec index = find(dE==DE);
    double r = dist(gen);
    if (r<=valE(index(0))){
      spinmat(x,y)*=-1;
      M +=2*spinmat(x,y);
      E += dE;
    }
  }
}

//Summerer spinnene rundt et gitt spinn
int nearsum(int x, int y, mat &spinmat,int L){
  int ssum = 0;
  for(int add = -1;add<=1;add+=2){
    ssum+=spinmat(periodic(x,add, L),y);
    ssum+=spinmat(x,periodic(y,add, L));
  }
  return ssum;
}

//Lager startmatrise med tilfeldig konfigurasjon eller spinn = 1
void init(int L,mat &spinmat,double &E,double &M,uniform_real_distribution<double> &dist, mt19937_64 &gen){
  for(int x = 0; x<L;x++){
    for(int y = 0; y < L; y++){
      double r = dist(gen);
      if (r <0.5){
        spinmat(x,y) = -1;
      }
      else {
        spinmat(x,y) = 1;
      }
    }
  }
  for(int x=0;x<L;x++){
    for(int y=0;y<L;y++){
      E-=spinmat(x,y)*(spinmat(periodic(x,1,L),y)+spinmat(x,periodic(y,1,L)));
      M+=spinmat(x,y);
    }
  }
}

//Skriver ut forventningsverdier
void outputexpect(int L, int maxmcc, double T, vec expval){
  double norm = 1.0/((double) (maxmcc));
  double E_calc = expval(0)*norm;
  double E2_calc = expval(1)*norm;
  double M_calc = expval(2)*norm;
  double M2_calc = expval(3)*norm;
  double absM_calc = expval(4)*norm;
  double Evar = (E2_calc - E_calc*E_calc)/L/L;
  double Mvar = (M2_calc - absM_calc*absM_calc)/L/L;
  ofile << setiosflags(ios::scientific | ios::uppercase);
  ofile << setw(17) << setprecision(8) << T<<endl;
  ofile << setw(17) << setprecision(8) << E_calc/L/L<<endl;
  ofile << setw(17) << setprecision(8) << Evar/T/T<<endl;
  ofile << setw(17) << setprecision(8) << M_calc/L/L<<endl;
  ofile << setw(17) << setprecision(8) << absM_calc/L/L<<endl;
  ofile << setw(17) << setprecision(8) << Mvar/T<<endl;
}
