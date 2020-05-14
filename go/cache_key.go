package main

import (
	"net/url"
	"strconv"
	"strings"
)

// this func is the default makeCacheKey, use SetMakeCacheKey to override it
func defaultMakeCacheKey(funcName string, version int64, strArgs []string, intArgs []int64) string {
	inputs := make([]string, len(strArgs)+len(intArgs)+2)
	inputs[0] = funcName
	inputs[1] = strconv.FormatInt(version, 10)
	offset := 2
	for i, arg := range strArgs {
		inputs[i+offset] = url.QueryEscape(arg)
	}
	offset = len(strArgs) + 2
	for i, arg := range intArgs {
		inputs[i+offset] = strconv.FormatInt(arg, 10)
	}
	return strings.Join(inputs, "&")
}

func main() {
	cacheKey := "lune-go" + defaultMakeCacheKey("AppVersionGetCurrent", 1, []string{"com.beeblio.sentence"}, []int64{1})
	print(cacheKey)
}
