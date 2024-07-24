s = "   Python is fun!   "

trimmed_s = s.strip()

leftjustified= trimmed_s.ljust(20, "*")

rightjustified= trimmed_s.rjust(20, "*")

print(trimmed_s)         # Python is fun!
print(leftjustified)  # Python is fun!*****
print(rightjustified) # *****Python is fun!
