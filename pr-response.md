# PR Response Doc — CineLog Watchlist Feature

## AI Usage
<!-- Fill in at the end — how you used AI tools during this project -->

## Comment 1 — Rename
**What I did:**
I changed the function save_to_watchlist in services/watchlist_service.py to add_to_watchlist to better conform to the naming conventions already used. It was only used in routes/watchlist/watchlist.py in the add_film endpoint
**How I verified:**
I used the vscode search function to check in all the files

## Comment 2 — Deduplication
**What I did:**
I added a query to check the watchlist to see if the film to be added is already in the watchlist
**How I verified:**
I did it in the same manner it is done in the add_to_collection file.

## Comment 3 — Missing test
**What I did:**
I created a new file with a test that checks to see if an error is raised upon adding a non-existent movie into the watchlist
**How I verified:**
I ran the test and it ap

## Comment 4 — Default visibility
**My position:**
My position is that the default visibility should be private.
**Reasoning:**
This is the user's watchlist, by default I believe that items in it should be private, as their watchlist should really just be for them, the comment under WatchlistEntry is "Represents a film a user wants to watch (saved for later)." The user is saving a movie that they want to watch later, it is a function that services themselves. By default it should be private, as we wouldn't want to accidentally expose these movies to the world
**Tradeoff acknowledged:**
By making privacy the default, those who want their watchlist to be public may have to go out of their way to do so.

## Comment 5 — Sort order
**My position:**
Sort order should remain in alphabetical order
**Reasoning:**
Alphabetical is much neater, looks nicer.
**Engagement with reviewer's point:**
Alphabetical order ensures that old movies that have been sitting in the watchlist for a long time won't stay there at the bottom forever. I feel as though by making it sorted by date added it would encourage people to only watch the newest movies at the top of the list, and make them forget about older movies. The watchlist should be there to remind people about movies they want to watch, you are not really reminding a person about a movie they added in just a day or two ago.

## Comment 6 — Rebase
**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description
<!-- Written at the end — feature overview, design decisions, manual testing steps -->