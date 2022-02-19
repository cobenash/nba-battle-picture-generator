from heapq import merge
from PIL import Image, ImageColor
from colorthief import ColorThief


class NbaBattle:
    TeamAbb = ['ATL', 'BOS', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MIA', 'MIL', 'MIN',
               'BKN', 'NYK', 'ORL', 'IND', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM', 'WAS', 'DET', 'CHA']

    def __init__(self, teamA, teamB):
        self.teamA = self._is_valid_team(teamA)
        self.teamB = self._is_valid_team(teamB)

    def _is_valid_team(self, team):
        if team not in self.TeamAbb:
            raise ValueError("Team's abbreviation is wrong.")
        return team

    def home_team_logo(self):
        logo = self.generate_team_picture(self.teamA)
        logo.show()

    def guest_team_logo(self):
        logo = self.generate_team_picture(self.teamB)
        logo.show()

    def generate_team_picture(self, team):
        logo_path = f"teams/{team}.png"
        team_logo = Image.open(logo_path)
        color_thief = ColorThief(logo_path)
        background_image = Image.new("RGB", (600, 600), color_thief.get_color(quality=1))
        team_logo = team_logo.convert("RGBA")
        background_image = background_image.convert("RGBA")
        width = (background_image.width - team_logo.width) // 2
        height = (background_image.height - team_logo.height) // 2
        background_image.paste(team_logo, (width, height), team_logo)
        background_image.save(f"generate/{team}.png", format="png")
        return background_image
