# Python WebScraping for CardMarket

## How it works

First, create a file named `secrets.json` and paste this content (edit with your data) :

```json
{
  "user": "YourUsername",
  "collection" : "YourGameCollection"
}
```

Then run
```bash
$ python3 ./main.py
```

The program parse the website every two hours and fill an output file `output.json` containing all the cards that might be similar to your sales proposition.
