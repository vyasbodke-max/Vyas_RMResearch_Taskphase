class tresurehunt:
   
 def __init__(self):
    self.tmap=[]
 def goto(self,row,col):
    print(f"I am currently at {row+1},{col+1}")
    r=(self.tmap[row][col]//10)-1
    c=(self.tmap[row][col]%10)-1
    if row==r and col==c:
           print(f"Treasure found at coordinates {r+1},{c+1}")
           return
    self.goto(r,c)
    
if __name__ =="__main__":
    hunt=tresurehunt()
    print("Enter the 5 rows of the treasure map spearated by spaces")
    for i in range(5):
        row=list(map(int,input().split()))
        hunt.tmap.append(row)
    hunt.goto(0,0)
    




