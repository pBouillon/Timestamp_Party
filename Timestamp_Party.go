package main

import (
	"fmt"
	"time"
)

func makeTimestamp() int64 {

    return time.Now().UnixNano() / int64(time.Millisecond)
}

func party() {
	fmt.Printf("%s\n","\n"+
    "************************\n"+
    "     Merry Timestamp !  \n"+
    "        1500000000      \n"+
    "************************"+
    "\n")
}

func main() {
	var awaited int32 = 1500000000 

	var cts, to_ts int32
	var run4ever bool = true

	for run4ever {
		cts   = int32(time.Now().Unix())
		to_ts = awaited - cts

		if to_ts <= 0 {
			run4ever = false
			party()
		}
		time.Sleep(1 * time.Second)
	}
}
