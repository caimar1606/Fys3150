/*
Dette er et program for å simulere to-spinn systemet for et LxL gitter med objekter som har spinn +-1
For å kjøre programmet må man sende med: L temperatur antallMCsykluser filnavnforventningsverdi filnavnvektorer
Man kan sende med et ekstra kommandolinjeargument for å ha spinn 1 startkonfigurasjon for alle objekter
, ellers er det tilfeldig startkonfigurasjon.

Legg merke til at dette programmet bare regner for en gitt T-verdi og er ikke parallellisert.
*/
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
void init(int,mat &,int &,int &,uniform_real_distribution<double> &, mt19937_64 &, int);
void sweep(int,int &,int &,int &,mat &,vec,vec,uniform_real_distribution<double> &, mt19937_64 &);
int nearsum(int, int, mat &,int);
void outputexpect(int, int ,double, vec);
void outputvec(int, int ,double, mat,string);

int main(int argc, char* argv[]){
  //Definisjoner av variabler og vektorer
  int E = 0;
  int M = 0;
  int nflips=0;
  int maxmcc = atof(argv[3]);
  int L = atof(argv[1]);
  double T = atof(argv[2]);
  double B = 1.0/T;
  vec DE = {8, 4, 0, -4, -8};
  vec valE = exp(-B*DE);
  vec expval = vec(5,fill::zeros);
  mat vecval = mat(7,maxmcc,fill::zeros);

  //Setter opp trekking av tilfeldige tall
  random_device rd;
  mt19937_64 gen(rd());
  uniform_real_distribution<double> dist(0.0,1.0);

  mat spinmat = mat(L,L);

  //If setning som starter spinn 1 startkonfigurasjon
  if(argc == 7){
    int val = 1;
    init(L,spinmat,E,M,dist,gen,val);
  }
  else{
    init(L,spinmat,E,M,dist,gen,0);
  }
  //For loop over mc sykluser

  clock_t start, finish;
  double time;

  double cps = CLOCKS_PER_SEC;
  start = clock();
  for(int count = 1;count<=maxmcc;count++){
    sweep(L,E,M,nflips,spinmat,valE,DE,dist,gen);
    expval(0) += E;
    expval(1) +=E*E;
    expval(2) += M;
    expval(3) += M*M;
    expval(4) += fabs(M);
    vecval(0,count-1) = expval(0)/count;
    vecval(1,count-1) = expval(1)/count;
    vecval(2,count-1) = expval(2)/count;
    vecval(3,count-1) = expval(3)/count;
    vecval(4,count-1) = expval(4)/count;
    vecval(5,count-1) = nflips;
    vecval(6,count-1) = E;
  }

  finish = clock();
  time = (finish - start)/cps;
  cout << "Tiden det tar med " << maxmcc << " Monte Carlo sykluser er " << time*1000 << "ms" << endl;
  string fileout = argv[4];
  string vecfileout = argv[5];
  ofile.open(fileout);
  //Skriver ut forventningsverdier
  outputexpect(L,maxmcc,T,expval);
  ofile.close();
  //Skriver ut vektorer som funksjon av sykluser
  outputvec(L,maxmcc,T,vecval,vecfileout);
}

//Gjør et utvalg av mulige tilfeldige spinnendringer LxL ganger og regner ut endringer i energi og magnetisk moment
void sweep(int L,int &E,int &M, int &nflips,mat &spinmat,vec valE,vec DE,uniform_real_distribution<double> &dist, mt19937_64 &gen){
  int Nmax = L*L;
  nflips = 0;
  for(int N=0;N<Nmax;N++){
    int x = int(floor(dist(gen)*L));
    int y = int(floor(dist(gen)*L));
    double dE = 2*spinmat(x,y)*nearsum(x,y,spinmat,L);
    uvec index = find(dE==DE);
    double r = dist(gen);
    if (r<=valE(index(0))){
      nflips +=1;
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
void init(int L,mat &spinmat,int &E,int &M,uniform_real_distribution<double> &dist, mt19937_64 &gen, int val){
if(val == 0){
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
}
else{
  spinmat = mat(size(spinmat),fill::ones);
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
  double Mvar = (M2_calc - M_calc*M_calc)/L/L;
  ofile << setiosflags(ios::scientific | ios::uppercase);
  ofile << setw(17) << setprecision(8) <<"Temperature: "<< T<<endl;
  ofile << setw(17) << setprecision(8) <<"Energy: "<< E_calc/L/L<<endl;
  ofile << setw(17) << setprecision(8) <<"Cv: "<< Evar/T/T<<endl;
  ofile << setw(17) << setprecision(8) <<"M-abs: "<< absM_calc/L/L<<endl;
  ofile << setw(17) << setprecision(8) <<"Sus: "<< Mvar/T<<endl;
}
//Skriver ut vektorer som funksjoner av Monte Carlo syklus
void outputvec(int L, int maxmcc, double T, mat vecval,string filename){
  vecval = vecval/L/L;
  string output;
  for(int i = 0;i<7;i++){
    output = filename+to_string(i);
    ofile.open(output);
    ofile << setiosflags(ios::scientific | ios::uppercase);
    ofile << setw(17)<<setprecision(8)<<vecval.row(i);
    ofile.close();

  }
}
