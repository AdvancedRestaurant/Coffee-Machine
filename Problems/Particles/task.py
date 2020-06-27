spin = input()
electron = input()

if spin == "1" and electron == "0":
    print("Photon Boson")
elif spin == "1/2" and electron == "0":
    print("Muon Lepton")
elif spin == "1/2" and electron == "-1":
    print("Electron Lepton")
elif spin == "1/2" and electron == "2/3":
    print("Charm Quark")
else:
    print("Strange Quark")
