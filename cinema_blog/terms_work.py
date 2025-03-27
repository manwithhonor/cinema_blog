from cinema_blog.models import Imdb, Authors

def get_terms_for_table():
    terms = []
    # lst = Imdb.objects.values('Series_Title', 'Released_Year')
    for i, item in enumerate(Imdb.objects.all()):
        terms.append([i + 1, item.Series_Title, item.Released_Year])
    return terms


def write_term(new_film, new_year):
    term = Imdb(Series_Title=new_film, Released_Year=new_year)
    term.save()

def write_user(user_name, user_email):
    term_addition = Authors(author_name=user_name, author_email=user_email)
    term_addition.save()

def get_terms_stats():
    db_terms = len(Imdb.objects.all())
    terms = Imdb.objects.all()
    defin_len = [len(term.Series_Title) for term in terms]
    stats = {
        "films_all": db_terms,
        "title_len_avg": round(sum(defin_len)/len(defin_len), 2),
        "title_len_max": max(defin_len),
        "title_len_min": min(defin_len)
    }
    return stats
