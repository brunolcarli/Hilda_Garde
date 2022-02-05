import re
import requests
import logging
from collections import OrderedDict
from difflib import SequenceMatcher
import discord
from discord.ext import commands, tasks
from hilda_garde.settings import __version__, ENDPOINTS


log = logging.getLogger(__name__)
client = commands.Bot(command_prefix='+')


@client.event
async def on_ready():
    log.info('Ok!')


@client.command(aliases=['v'])
async def version(ctx):
    """
    Returns bot version.
    """
    await ctx.send(__version__)


@client.command(aliases=['tn'])
async def tournament(ctx, tournament_id):
    """
    Returns tournament information by the tournament ID.
    """
    url = f'{ENDPOINTS["tournaments"]}{tournament_id}'
    response = requests.get(url).json()

    parser = re.compile('<.*?>')
    embed = discord.Embed(color=0x1E1E1E, type="rich")
    banner_pic = response.get('bannerUrl')
    embed.set_thumbnail(url=banner_pic)

    embed.add_field(name='Game', value=response.get('gameName'), inline=True)
    embed.add_field(name='Start Datetime', value=response.get('startTime'), inline=True)
    embed.add_field(name='Players per team', value=response.get('playersPerTeam'), inline=True)
    embed.add_field(name='Region', value=response.get('region'), inline=True)
    
    about = re.sub(parser, '\n', response.get('about', ''))
    embed.add_field(name='About', value=about, inline=False)

    return await ctx.send(f'**{response.get("name")}**', embed=embed)


@client.command(aliases=['teams'])
async def tournament_teams(ctx, tournament_id):
    """
    Return registered teams on a given tournament.
    """
    url = f'{ENDPOINTS["tournaments"]}{tournament_id}/teams'
    response = requests.get(url).json()

    embed = discord.Embed(color=0x1E1E1E, type="rich")

    for team in response:
        embed.add_field(name=team['name'], value=f'ID: {team["_id"]}', inline=True)
    
    return await ctx.send('Teams for tournament:', embed=embed)


@client.command(aliases=['players'])
async def tournament_players(ctx, tournament_id, team_id):
    """
    Return players of a team in a tournament.
    """
    url = f'{ENDPOINTS["tournaments"]}{tournament_id}/teams'
    response = requests.get(url).json()

    embed = discord.Embed(color=0x1E1E1E, type="rich")

    for team in response:
        if not (team['_id'] == team_id):
            continue
        embed.add_field(name='Name', value=team['name'], inline=True)
        embed.add_field(name='Captain', value=team['captain']['username'], inline=True)
        players = '\n'.join(p['username'] for p in team['players'])
        embed.add_field(name='Players', value=players, inline=False)
        embed.set_thumbnail(url=team['persistentTeam']['logoUrl'])
    
    return await ctx.send('Team general view:', embed=embed)


@client.command(aliases=['cp', 'games'])
async def campaigns(ctx, *game_name):
    """
    Returns ongoing campaigns.
    """
    game_name = ' '.join(token for token in game_name).strip()
    url = ENDPOINTS['campaigns']
    response = requests.get(url).json()
    
    embed = discord.Embed(color=0x1E1E1E, type="rich")

    # if no param specified list all available games
    if not game_name:
        for game in response:
            embed.add_field(name='Name', value=game['name'], inline=True)
        
        return await ctx.send('Available games:', embed=embed)

    # Else, show game detailed information
    priority = {}
    for game in response:
        ratio = SequenceMatcher(None, game_name, game['name']).ratio()
        priority[ratio] = game

    # order the data for param similarity
    priority = OrderedDict(sorted(priority.items(), reverse=True))

    game_data = list(priority.items())[0][1]
    embed.set_thumbnail(url=game_data['imageUrl'])
    embed.add_field(name='Name', value=game_data['name'], inline=True)
    embed.add_field(name=':medal: Prizing:', value=game_data['properties'].get('prizing', '-'), inline=True)
    embed.add_field(name='Start Date', value=game_data['properties'].get('startDate', '-'), inline=True)
    embed.add_field(name='Link URL', value=game_data['linkUrl'], inline=True)

    return await ctx.send('Campaign info:', embed=embed)
