<table align="center"><tr><td align="center" width="9999">

<img src="https://i.pinimg.com/600x315/fd/cc/26/fdcc26928abc213a03fba4536b7b2fa9.jpg" align="center" width="150" alt="Project icon">

# Hilda Garde

*Battlefy platform bot integration for discord*
</td></tr></table>


<div align="center">

> [![Version badge](https://img.shields.io/badge/version-0.0.1-silver.svg)]()

</div>

[Hilda Garde](https://finalfantasy.fandom.com/wiki/Hilda_Garde#Hilda_Garde_I) is a discord bot which consumes data from Battlefy (e-sports platform) to present on discord, such as ongoing tournaments, campaigns, teams and players.

## Usage

You can add the bot to a discord server of your preference with this [invite](https://discord.com/api/oauth2/authorize?client_id=939520804033536040&permissions=378880&scope=bot).

The bot command prefix is `+`.

The most simple command to test bot response is `+version` which returns the current bot version:

![version_command](https://uploaddeimagens.com.br/images/003/708/145/full/Captura_de_Tela_2022-02-05_a%CC%80s_13.52.14.png?1644080083)

### View tournament

To view a tournament information it s necessary to inform the tournament id as an argument for the bot command `+tournament`. The id (by now) must be collected on the Battlefy platform (while a database tool to register these IDs is not implemented):

![collect tournament id](https://static.invenglobal.com/upload/image/2019/07/05/r1562343292250060.png)

And use this hash id on the command:

![tournament_command](https://uploaddeimagens.com.br/images/003/708/153/full/Captura_de_Tela_2022-02-05_a%CC%80s_14.01.50.png?1644080529)


### View registered teams on a tournament

To list the current registered teams on a given tournament is pretty much the same as the previous command, just use the tournament id as argument to the `+tournament_teams` command:


![teams](https://uploaddeimagens.com.br/images/003/708/162/full/Captura_de_Tela_2022-02-05_a%CC%80s_14.04.50.png?1644080800)


To view detailed information about the team and its members, use the tournament id followed by the team id on the command `+tournament_players`:

![players](https://uploaddeimagens.com.br/images/003/708/164/full/Captura_de_Tela_2022-02-05_a%CC%80s_14.08.52.png?1644080978)

### View campaigns

To list ongoing available campaigns use the command `+campaigns`:

![list campaigns](https://uploaddeimagens.com.br/images/003/708/166/full/Captura_de_Tela_2022-02-05_a%CC%80s_14.11.06.png?1644081147)

To see more detailed information about a campaign, use the same command followed by the name (full or partially) of the campaign:

![campaign info](https://uploaddeimagens.com.br/images/003/708/167/full/Captura_de_Tela_2022-02-05_a%CC%80s_14.11.32.png?1644081250)


A full list of the available commands is returned with the command `+help`. Detailed information about a specific command is retrieved with `+help command_name`, i.e `+help tournaments`.

## Development

This is an open source project, if you are a developer (or aspiring to be one), feel free to run, modify, enhance or add new features. First of all you will need a bot token, which you can get by creating an application on [discord developers portal](https://discord.com/developers/applications) for free.

Create a new [python virtual environment](https://docs.python.org/3/library/venv.html) and install the required dependencies:

On Linux/MacOS:

```
$ make install
```

On windows:

```
> pip install -r hilda_garde/requirements/development.txt
```

Then export the token you get on discord developers as an ENV VAR:

```
$ export TOKEN=dasigdasiugdguasgiuasigudgasiudasd
```

 
> :bulb: Dont forget to use **your token** on the mentioned command above! :bulb:

Finally run the service:

On Linux/MacOS:

```
$ make run
```

On Windows:

```
> python3 main.py
```
