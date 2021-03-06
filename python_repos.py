import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#API call and storing the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

#Storing API response in a variable
response_dict = r.json()
print("Total Repositories: ", response_dict['total_count'])

#Exploring information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))


#Examininig the first repository, 
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))

names, plot_dicts = [],[]


"""printing information and knowing about all repositories returned by the api call """

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    #Getting project description
    description = repo_dict['description']
    if not description:
        description = 'NO Description Provided.'

    plot_dict = {
    'value': repo_dict['stargazers_count'], 
    'label': repo_dict['description'],
    'xlink': repo_dict['html_url'],
    }

    plot_dicts.append(plot_dict)


#Making Visualization
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
