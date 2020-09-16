import discord
import json
import os
import re
import datetime
import traceback
import random
import asyncio
from discord.ext import commands
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

bot_two = commands.Bot(command_prefix = '>')






@bot_two.event
async def on_ready():
    await bot_two.change_presence(activity=discord.Watching(name="General Chat!"))
    print('<------------------------------>')
    print('Coding Comunity Bot is ready')
    print('<------------------------------>')




has_avatar = commands.check(lambda ctx: ctx.avatar_url != ctx.author.default_avatar_url)

@has_avatar
@bot_two.event
async def on_member_join(member):
        try:
            alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
            numeric = ('1','2','3','4','5','6','7','8','9','0')
            final = []

            member = member
            for i in range(6):
                des = ('alpha', 'numeric')
                an = random.choice(des)
                if an == 'alpha':
                    a = random.choice(alpha)
                    cap = ('lower', 'upper')
                    caps = random.choice(cap)
                    if caps == 'lower':
                        final.append(a.lower())
                    else:
                        final.append(a.upper())
                else:
                    a = random.choice(numeric)
                    final.append(a)
            code = ''.join(map(str, final))
            if code.isnumeric() == True:
                print('Nope')
            else:
                img = Image.new('RGB', (360, 180), color = 'white')

                d = ImageDraw.Draw(img)
                font = ImageFont.truetype("Futura.ttf", 90)
                d.text((3, 9.2), f"{code}", font=font, fill=(0,0,0))
                img.save('back.png')


            embed = discord.Embed(title='Type the code below to get verified!')
            embed.set_image(url="attachment://back.png")
            image = discord.File("back.png")
            await member.send(embed=embed, file=image)
            if member.id == None:
                await asyncio.sleep(5)
                print('made it 1')
                def check(x):
                    return x.author == member
                print('made it 2')
                verif = await bot_two.wait_for('message',check = check, timeout = 300)
                print(verif)
                if verif.content == code:
                    await member.send('You passed the verification process!')
                else:
                    await member.send('You failed the verification process!\nTry again!')
        except Exception:
            traceback.print_exc()


@bot_two.command()
async def warn(ctx , member : discord.Member ,* , reason = "No reason Provided"):
  with open('warnings.json','r') as f:
    warns = json.load(f)
  if str(ctx.guild.id) not in warns:
    warns[str(ctx.guild.id)] = {}
  if str(member.id) not in warns[str(ctx.guild.id)]:
    warns[str(ctx.guild.id)][str(member.id)] = {}
    warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
    warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
  else:
    warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
  with open('warnings.json','w') as f:
    json.dump(warns , f)
    await ctx.send(f"{member.mention} was warned for: {reason}")
    
    embed = discord.Embed(title='You have been warned in The Coding Community', description=f'You received a warning from {member}')
    embed.add_field(name='Reason:', value=f'{reason}')
    await member.send(embed=embed)
    
@bot_two.command()
async def removewarn(ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
  with open('warnings.json' , 'r') as f:
    warns = json.load(f)
  num -= 1
  warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
  warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
  with open('warnings.json' , 'w') as f:
    json.dump(warns , f)
    await ctx.send('Warn has been removed!')
    embed = discord.Embed(title='Your warn in The Coding Community has been removed', description=f'Your warning was removed by {ctx.author}')
    await member.send(embed=embed)

        
@bot_two.command()
async def warns(ctx , member : discord.Member):
  with open('warnings.json', 'r') as f:
    warns = json.load(f)
  num = 1
  warnings = discord.Embed(title = f"{member}\'s warns")
  for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
    warnings.add_field(name = f"Warn {num}" , value = warn)
    num += 1
  await ctx.send(embed = warnings)


@bot_two.command()
async def verify(ctx):
        try:
            alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
            numeric = ('1','2','3','4','5','6','7','8','9','0')
            final = []

            member = ctx.author
            for i in range(6):
                des = ('alpha', 'numeric')
                an = random.choice(des)
                if an == 'alpha':
                    a = random.choice(alpha)
                    cap = ('lower', 'upper')
                    caps = random.choice(cap)
                    if caps == 'lower':
                        final.append(a.lower())
                    else:
                        final.append(a.upper())
                else:
                    a = random.choice(numeric)
                    final.append(a)
            code = ''.join(map(str, final))
            if code.isnumeric() == True:
                print('Nope')
            else:
                img = Image.new('RGB', (360, 180), color = 'white')

                d = ImageDraw.Draw(img)
                font = ImageFont.truetype("Futura.ttf", 90)
                d.text((3, 9.2), f"{code}", font=font, fill=(0,0,0))
                img.save('back.png')


            embed = discord.Embed(title='Type the code below to get verified!')
            embed.set_image(url="attachment://back.png")
            image = discord.File("back.png")
            await member.send(embed=embed, file=image)
            ctx.guild = None
            if ctx.guild == None:
                await asyncio.sleep(5)
                print('made it 1')
                def check(x):
                    return x.author == ctx.author
                print('made it 2')
                verif = await bot_two.wait_for('message',check = check, timeout = 300)
                print(verif)
                if verif.content == code:
                    await member.send('You passed the verification process!')
                else:
                    await member.send('You failed the verification process!\nTry again!')
        except Exception:
            traceback.print_exc()

bot_two.run('')