import burstiness
import perplexity
import argparse
import ASCII
from os.path import isfile
import BetterRich
import features
import joblib
import reporter

parser = argparse.ArgumentParser(description="AI text detector")
parser.add_argument("-t", "--text", help="Text to scan", required=False)
parser.add_argument("-f", "--textFile", help="Text file to scan", required=False)
parser.add_argument("-d", "--debugmode", action='store_true', help="debugmode for full error text", required=False)
arg = parser.parse_args()
debug = arg.debugmode

Database = joblib.load("modelDB.pkl")

print(ASCII.print_banner())

try:
    if arg.text is not None:
        try:
            features = features.extract(arg.text)
            result = Database.predict([features])
            reporter.report(result)

        except Exception as e:
            if debug is True:
                print(e)
            else:
                BetterRich.warn("ERROR! For more information, use debugmode")
    else:
        if arg.textFile is None:
            BetterRich.warn("No File or text to scan!")
        else:
            if isfile(arg.textFile) is False:
                BetterRich.warn("FILE INPUT IS WRONG!")
            else:
                if isfile(arg.textFile) is True:
                    try:
                        with open(arg.textFile, "r") as f:
                            ft = f.read()

                        features = features.extract(ft)
                        result =  Database.predict([features])
                        reporter.report(result)
                    except Exception as e:
                        if debug is True:
                            print(e)
                        else:
                            BetterRich.warn("ERROR! For more information, use debugmode")
except Exception as e:
    if debug is True:
        print(e)
    else:
        BetterRich.warn("ERROR! For more information, use debugmode")