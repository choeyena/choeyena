import pickle

outfile = open("test.dat", "wb")
pickle.dump(12, outfile)
pickle.dump(3.14, outfile)
pickle.dump([1, 2, 3, 4, 5], outfile)
outfile.close() 

infile = open("test.dat", "rb")
print(pickle.load(infile))
print(pickle.load(infile))
print(pickle.load(infile))
infile.close() 