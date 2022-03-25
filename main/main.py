import turtle
import os
import random
import pandas as pd
import dataframe_image as dfi
from PIL import Image
import glob

screen=turtle.Screen()
screen.setup(1500, 800)
screen.title("Best seller book matcher!")
image=os.path.join("images","NYT_BestSeller.gif")
books=os.path.join("output","combined_book2.csv")
df=pd.read_csv(books)

def main_categories(x):
  
    if x in ["Hardcover Fiction","Hardcover Nonfiction","Combined Print Nonfiction","Combined Print Fiction"]:
        return "Printed"

    elif x in ["Audio Fiction","Audio Nonfiction"]:
        return "Audio"

    else:
        return "E_book"

    
def fiction_or_not_detector(x):
    if x in ["Hardcover Fiction","Combined Print Fiction","E-Book Fiction","Audio Fiction"]:
        return "Fiction"
    
    elif x in ["Hardcover Nonfiction","Combined Print Nonfiction","E-Book Nonfiction","Audio Nonfiction"]:
        return "Nonfiction"


df['Fic_or_NotFic']= df['category'].apply(fiction_or_not_detector)
df["Main_category"]=df['category'].apply(main_categories)


screen.addshape(image)
turtle.shape(image)

fic_or_not=screen.textinput(title="fic_or_not",prompt="Fiction or Nonfiction? put fiction/nonfiction")
audio_ebook_printd=screen.textinput(title="audio_ebook_printd",prompt="Which one you prefer?Audio, E_book or Printed? put audio/e_book/printed")
price=screen.textinput(title="price",prompt="The maximum book price you are looking? put 30/60/100")

for i in ['Audio','E_book','Printed']:
    for j in ["30","60","100"]:
        for k in ["Fiction","Nonfiction"]:
            if audio_ebook_printd.capitalize()==i and price==j and fic_or_not.capitalize()==k:
                res=df.loc[(df['Main_category']==i)&(df['Fic_or_NotFic']==k)&(df['Amazon Price']>=0)&(df['Amazon Price']<int(j))]\
                     [["title","author","Amazon Rating","Amazon Rating Total","Amazon Price","category"]].sort_values(by="Amazon Rating Total", ascending=False).set_index('title').head(10)
                book=f'Most popular {k} books in {i} category with Maximum price of ${j}: '

           
        

dfi.export(res,"images/mytable.png")
frames = []
imgs = glob.glob("images/mytable.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
frames[0].save('images/mytable.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)

screen.update()
screen.setup(1500, 800)
screen.title("Best seller book matcher!")
image=os.path.join("images","mytable.gif")
screen.addshape(image)
turtle.shape(image)

t2=turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.goto(-500,300)
t2.color('navy')
t2.write(f'{book}',font=('Courier', 20, 'bold'))    
screen.exitonclick()