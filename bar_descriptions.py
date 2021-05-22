import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'Python Projects'
chart.x_labels = ['system-design-…', 'public-apis', 'awesome-python']

plot_dicts = [
    {'value': 103845, 'label': 'Description of system-design-…'},#pluggin in values manually with respect to our old python_repos graph
    {'value': 91920, 'label': 'Description of public-apis'},#pluggin in values manually with respect to our old python_repos graph
    {'value': 85335, 'label': 'Description of awesome-python'},#pluggin in values manually with respect to our old python_repos graph
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')

