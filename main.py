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
        return "E-Book"

    
def fiction_or_not_detector(x):
    if x in ["Hardcover Fiction","Combined Print Fiction","E-Book Fiction","Audio Fiction"]:
        return "Fiction"
    
    elif x in ["Hardcover Nonfiction","Combined Print Nonfiction","E-Book Nonfiction","Audio Nonfiction"]:
        return "Nonfiction"


df['Fic_or_NotFic']= df['category'].apply(fiction_or_not_detector)
df["Main_category"]=df['category'].apply(main_categories)


screen.addshape(image)
turtle.shape(image)

fic_or_not=screen.textinput(title="fic_or_not",prompt="Fiction or Non fiction? put f/n")
audio_ebook_printd=screen.textinput(title="audio_ebook_printd",prompt="Which one you prefer?Adiou, E_book or Printed? put a/e/p")
price=screen.textinput(title="price",prompt="The maximum book price you are looking? put 30/60/90")

if price=='30' and audio_ebook_printd=='a' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Audio category with Maximum price of $30: '
        
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Audio category with Maximum price of $30: '
        
    else:
        book="please try again"
elif price=='60' and audio_ebook_printd=='a' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Audio category with Maximum price of $60: '
        
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Audio category with Maximum price of $60: '
        
    else:
        book="please try again"

elif price=='90' and audio_ebook_printd=='a' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Audio category with Maximum price of $90: '
        
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Audio')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Audio category with Maximum price of $90: '
        
    else:
        book="please try again"

elif price=='30' and audio_ebook_printd=='e' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in E-Book category with Maximum price of $30: '
        
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in E-Book category with Maximum price of $30: '
    else:
        book="please try again"
elif price=='60' and audio_ebook_printd=='e' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in E-Book category with Maximum price of $60: '
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in E-Book category with Maximum price of $60: '
    else:
        book="please try again"

elif price=='90' and audio_ebook_printd=='e' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in E-Book category with Maximum price of $90: '
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='E-Book')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in E-Book category with Maximum price of $90: '
    else:
        book="please try again"


elif price=='30' and audio_ebook_printd=='p' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Printed category with Maximum price of $30: '
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<30)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Printed category with Maximum price of $30: '
    else:
        book="please try again"
elif price=='60' and audio_ebook_printd=='p' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Printed category with Maximum price of $60: '
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<60)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Printed category with Maximum price of $60: '
    else:
        book="please try again"

elif price=='90' and audio_ebook_printd=='p' :
    if fic_or_not=="f":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Fiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Fiction books in Printed category with Maximum price of $90: '
    elif fic_or_not=="n":
        res=df.loc[(df['Main_category']=='Printed')&(df['Fic_or_NotFic']=='Nonfiction')&(df['Amazon Price']>=0)&(df['Amazon Price']<90)]\
            .head(10)[["title","author","Amazon Rating","Amazon Rating Total","Amazon Price"]].sort_values(by="Amazon Rating", ascending=False).set_index('title')
        book=f'Nonfiction books in Printed category with Maximum price of $90: '
    else:
        book="please try again"




#df_styled = res.style.background_gradient()
dfi.export(res,"images/mytable.png")
frames = []
imgs = glob.glob("images/mytable.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
# Save into a GIF file that loops forever
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