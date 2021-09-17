from os import scandir
from fibonacci import Fibonacci

INfilename = "FIBISTR.INP"
OUTfilename = "FIBISTR.OUT"

with open(INfilename, "r") as in_file:
    in_contents = in_file.readlines()

out_file = open(OUTfilename, "w")

for j in range (len(in_contents)):
    in_contents[j] = in_contents[j].strip()
    F_obj = Fibonacci(in_contents[j])
    Fstring = F_obj.getFk()
    Scount = F_obj.countSstring(Fstring)
    print(Fstring, F_obj.Sstring , Scount)
    out_file.write(f"{str(Scount)}\n")
print(f"\n-- DONE --\nFind result in {OUTfilename} file")
out_file.close()