
Earthsun.exe lager tolegemesystemet med jorda og kjøres som:

  ./earthsun.exe timestep output

  eks:
  ./earthsun.exe 0.0001 0_0001


all.exe lager systemet for alle planetene og kjøres som:

  ./all.exe timestep output finaltime

  eks:
  ./all.exe 0.0001 0_0001 100


beta.exe lager tolegemesystem med forskjellig betaverdi for en planet ved 1 AU og kjøres som:

  ./beta.exe timestep output finaltime beta

  eks:
  ./beta.exe 0.0001 0_0001 100 2.5

escape.exe lager tolegemesystem med forskjellig hastighet for planet ved 1AU og kjøres som:

  ./escape.exe timestep output velocity finaltime

  eks:
  ./escape.exe 0.0001 0_0001 100 9

mercury.exe lager tolegemesystem med merkur og kjøres som:

  ./mercury.exe timestep output rel
  Der rel = 0 gir ikke relativistisk, og alle andre verdier gir relativistisk

  eks:
  ./mercury.exe 0.0001 0_0001 1

three.exe lager trelegemesystem med jorda og jupiter og kjøres som:

  ./three.exe timestep output timesjupitermass

  eks:
  ./three.exe 0.0001 0_0001 10
