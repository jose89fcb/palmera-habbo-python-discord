import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def palmera(ctx, *, keko):
    await ctx.message.delete()
    await ctx.send("Generando palmera🌴...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit,crr=667&direction=2&head_direction=2&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    trozo = Image.open(r"imagenes/trozo.png").convert("RGBA") #imagen del trozo de silla
    img1 = trozo.resize((10,14), Image.ANTIALIAS)#tamaño del trozo

    palmera = Image.open(r"imagenes/palmera.png").convert("RGBA") #imagen de la palmera
    img1 = palmera.resize((100,160), Image.ANTIALIAS)#tamaño de la silla palmera

    ##
   
    ##

    
    

    
    

    img1.paste(palmera,(0,0), mask = palmera) #Posicion de la palmera

    img1.paste(img2,(29,44), mask = img2) #Posicion del keko 1
    img1.paste(trozo,(0,0), mask = trozo) #Posicion del trozo de silla
    ###
    

   

 
    
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   
