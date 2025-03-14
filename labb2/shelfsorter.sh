#!/bin/bash
FILENAME="$2" # New variable to hold the filename

    if [ "$1" == "--help" ];
        then    
        echo "Usage: shelfsorter [-p|-s {i|n|v|l|b|h}]"
        echo "Used primarily for sorting furniture "
        echo "  -p      print data contents and exit"
        echo "  -s      sort by additional argument: id (i)"
        echo "              name (n), weight (v), length (l)"
        echo "              width (b), height (h), print data"
        echo "              contents and exit"
        echo "  --help display this help and exit"

    fi

    if [ "$1" == "-p" ];
        then    
        
        cat "$FILENAME"

    fi

    if [ "$1" == "-s" ];
        then   

        if [ "$2" == "i" ];
        then

            sort -n -t "," -k 1 "$FILENAME" | sed 's/,/ /g'  | column -t -s ','

        fi

        if [ "$2" == "n" ];
        then

            sort -t "," -k 2 "$FILENAME" | sed 's/,/ /g' | column -t -s ','

        fi
         
        if [ "$2" == "v" ];
        then

            sort -n -t "," -k 3 "$FILENAME" | sed 's/,/ /g'  | column -t -s ','

        fi

        if [ "$2" == "l" ];
        then
            
            sort -n -t "," -k 4 "$FILENAME" | sed 's/,/ /g' | column -t -s ','

        fi

        if [ "$2" == "b" ];
        then

            sort -n -t "," -k 5 "$FILENAME" | sed 's/,/ /g' | column -t -s ','

        fi

        if [ "$2" == "h" ];
        then

            sort -n -t "," -k 6 "$FILENAME" | sed 's/,/ /g'  | column -t -s ','

        fi

    fi
