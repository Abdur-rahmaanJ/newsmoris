
from newsmoris import DefiMedia

import click

@click.group(help="Newsmoris cli")
def cli():
    pass


# @click.command(help="<Empty, plain repo />")
# @click.argument('project_name')
# @click.option('--existing/--not-existing', default=False)
# def plain(project_name, existing):
#     path = '.'

#     dirs_exist_ok = False
#     if existing is True:
#         dirs_exist_ok = True
#     trycopytree(
#         os.path.join(sites_path, 'plain'),
#         os.path.join(path, project_name),
#         dirs_exist_ok=dirs_exist_ok
#         )


# @click.command(help="<Repo by templates />")
# @click.argument('template')
# @click.argument('project_name')
# @click.option('--existing/--not-existing', default=False)
# def t(template, project_name, existing):
#     path = '.'

#     namespace = template.split('/')[0]
#     project = template.split('/')[1]

#     dirs_exist_ok = False
#     if existing is True:
#         dirs_exist_ok = True
#     trycopytree(
#         os.path.join(sites_path, namespace, project),
#         os.path.join(path, project_name),
#         dirs_exist_ok=dirs_exist_ok
#         )


# cli.add_command(plain)
# cli.add_command(t)


@click.command(help="Top news")
def topnews():
    for info in DefiMedia.top_news():
        print(info['title'], info['link'], sep='\n', end='\n\n')


@click.command(help="Choose category from actualites, explikouka, faits-divers, defi-zen, politique, people, magazine, magazine, news-sunday, techno")
@click.argument('category')
@click.argument('page_num', type=int)
def page(category, page_num):
    for info in DefiMedia.page(category, page_num):
        print(info['title'], info['link'], sep='\n', end='\n\n')


@click.command(help="Input url")
@click.argument('article')
def article(article):
    info = DefiMedia.article(article)
    print('Written by', info['author'])
    for p in info['paragraphs']:
        print(p)

@click.command(help="Random Article")
def random():
    article = DefiMedia.random_article()
    print(article['title'], article['link'], sep='\n', end='\n\n')

cli.add_command(topnews)
cli.add_command(page)
cli.add_command(article)
cli.add_command(random)

def main():
    cli()

if __name__ == "__main__":
    cli()
