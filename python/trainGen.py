#!/usr/bin/python
# Usage: python trainGen.py -i annotated-classes -t 0.8 -s 123456 -b /content/darknet/


import sys, getopt, os, math, random

def main(argv):
   inputfolder = ''
   trainRatio =  0.7
   seed=2018
   base = 'test'
   try:
      opts, args = getopt.getopt(argv,"hi:t:s:b",["ifile=","tRatio=","seed=","base="])
   except getopt.GetoptError:
      print('trainGen.py -i <Data folder> [-t <Ratio train-test> -s <Random seed> -b <base absolute path>]')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('This script needs to be added at the same level as \nthe folder containing the annotated images, the default ratio is 0.7 (70% train 30% test)\nand the default value for seed is 2018\n\tCommand format (-i required, -t and -s optional ): \n\ttrainGen.py -i <Data folder> [-t <Ratio train-test> -s <Random seed>]')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfolder = arg
      elif opt in ("-t", "--tRatio"):
         try:
             trainRatio = float(arg)
             if trainRatio>=1:
                raise ValueError()
         except ValueError:
             print('Invalid ratio input, must be float and < 1')
             sys.exit()
      elif opt in ("-s", "--seed"):
         try:
            seed = int(arg)
         except ValueError:
            print('Invalid seed input, must be an int')
            sys.exit()
      elif opt in ("-b", "--base"):
         base = arg
         print('Base is ', base)
   random.seed(seed)
   train = open("train.txt","w+")
   test = open("test.txt","w+")
   for folder in os.listdir(inputfolder):
       folder_path=os.path.join(inputfolder,folder)
       fList=os.listdir(folder_path)
       i=0
       tSize=math.ceil(len(fList)*trainRatio)
       fList=random.sample(fList,len(fList))
       for file_path in fList:
           if ".jpg" in file_path:
               if i < tSize:
                   train.write(os.path.join(base,folder_path,file_path)+"\n")
               else:
                   test.write(os.path.join(base,folder_path,file_path)+"\n")
           elif ".png" in file_path:
               if i < tSize:
                   train.write(os.path.join(base,folder_path,file_path)+"\n")
               else:
                   test.write(os.path.join(base,folder_path,file_path)+"\n")
           i+=1 
   train.close()
   test.close()
       

if __name__ == "__main__":
   main(sys.argv[1:])