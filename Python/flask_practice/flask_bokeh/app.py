# https://medium.com/better-programming/deploy-interactive-real-time-data-visualizations-on-flask-with-bokeh-311239273838
# https://gist.github.com/m-bagley1020/a1c9ea830241bd6a0a20acdddac461f9

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

source = ColumnDataSource()

fig = figure(plot_height=600, plot_width=720, tooltips=[("Title", "@title"), ("Released", "@released")])
fig.circle(x="x", y="y", source=source, size=8, color="color", line_color=None)
fig.xaxis.axis_label = "IMDB Rating"
fig.yaxis.axis_label = "Rotten Tomatoes Rating"

currMovies = [
    {'imdbid': 'tt0099878', 'title': 'Jetsons: The Movie', 'genre': 'Animation, Comedy, Family', 'released': '07/06/1990', 'imdbrating': 5.4, 'imdbvotes': 2731, 'country': 'USA', 'numericrating': 4.3, 'usermeter': 46},
    {'imdbid': 'tt0099892', 'title': 'Joe Versus the Volcano', 'genre': 'Comedy, Romance', 'released': '03/09/1990', 'imdbrating': 5.6, 'imdbvotes': 23680, 'country': 'USA', 'numericrating': 5.2, 'usermeter': 54},
    {'imdbid': 'tt0099938', 'title': 'Kindergarten Cop', 'genre': 'Action, Comedy, Crime', 'released': '12/21/1990', 'imdbrating': 5.9, 'imdbvotes': 83461, 'country': 'USA', 'numericrating': 5.1, 'usermeter': 51},
    {'imdbid': 'tt0099939', 'title': 'King of New York', 'genre': 'Crime, Thriller', 'released': '09/28/1990', 'imdbrating': 7, 'imdbvotes': 19031, 'country': 'Italy, USA, UK', 'numericrating': 6.1, 'usermeter': 79},
    {'imdbid': 'tt0099951', 'title': 'The Krays', 'genre': 'Biography, Crime, Drama', 'released': '11/09/1990', 'imdbrating': 6.7, 'imdbvotes': 4247, 'country': 'UK', 'numericrating': 6.4, 'usermeter': 82}
]

source.data = dict(
    x = [d['imdbrating'] for d in currMovies],
    y = [d['numericrating'] for d in currMovies],
    color = ["#FF9900" for d in currMovies],
    title = [d['title'] for d in currMovies],
    released = [d['released'] for d in currMovies],
    imdbvotes = [d['imdbvotes'] for d in currMovies],
    genre = [d['genre'] for d in currMovies]
)

output_file("graph.html")
show(fig)

if __name__ == "__main__":
    app.run(debug=True)