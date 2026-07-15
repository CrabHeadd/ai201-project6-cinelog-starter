"""
services/watchlist_service.py — CineLog (feature/watchlist branch)

Business logic for the watchlist feature.
"""

from app import db
from models import Film, WatchlistEntry
from services.collection_service import FilmNotFoundError

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7de99ad (feat: Handling duplicate movies in watchlist)
class AlreadyInWatchlistError(Exception):
    """Raised when a film is already in the user's watchlist."""
    pass

def add_to_watchlist(user_id, film_id):
=======

<<<<<<< HEAD
def save_to_watchlist(user_id, film_id):
>>>>>>> ec90edb (added watchlist model and endpoint)
=======
def add_to_watchlist(user_id, film_id):
>>>>>>> d81965f (chore: changed save_to_watchlist to add_to_watchlist)
    """
    Save a film to a user's watchlist.

    Args:
        user_id (str): UUID of the user.
        film_id (int): ID of the film. (Note: integer — pre-refactor)

    Returns:
        WatchlistEntry: The newly created entry.

    Raises:
        FilmNotFoundError: If film_id does not exist.
    """
<<<<<<< HEAD
<<<<<<< HEAD
    film = db.session.get(Film, film_id)
    if film is None:
        raise FilmNotFoundError(f"No film found with id '{film_id}'")

    existing = WatchlistEntry.query.filter_by(
        user_id=user_id, film_id=film_id
    ).first()
    if existing:
        raise AlreadyInWatchlistError(
            f"Film '{film_id}' is already in this user's watchlist"
        )

<<<<<<< HEAD
=======
    film = Film.query.get(film_id)
=======
    film = db.session.get(Film, film_id)
>>>>>>> 7c37bcd (fix: update film retrieval method to use db.session.get in collection and watchlist services)
    if film is None:
        raise FilmNotFoundError(f"No film found with id '{film_id}'")

>>>>>>> ec90edb (added watchlist model and endpoint)
=======
>>>>>>> 7de99ad (feat: Handling duplicate movies in watchlist)
    entry = WatchlistEntry(user_id=user_id, film_id=film_id)
    db.session.add(entry)
    db.session.commit()
    return entry


def get_watchlist(user_id):
    """
    Return all films on a user's watchlist.

    Args:
        user_id (str): UUID of the user.

    Returns:
        list[dict]: List of film dicts with watchlist metadata attached.
    """
    entries = (
        WatchlistEntry.query
        .filter_by(user_id=user_id)
        .join(Film)
        .order_by(Film.title.asc())
        .all()
    )

    result = []
    for entry in entries:
        film_dict = entry.film.to_dict()
        film_dict["date_added"] = entry.date_added.isoformat()
        film_dict["public"] = entry.public
        result.append(film_dict)

    return result
