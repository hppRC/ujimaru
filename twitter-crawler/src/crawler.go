// package main

// import (
// 	"fmt"
// 	"html"
// 	"log"
// 	"net/url"
// 	"os"
// 	"regexp"
// 	"strings"
// 	"time"

// 	"github.com/hpprc/anaconda"
// 	"github.com/kelseyhightower/envconfig"
// )

// type specification struct {
// 	APIKey            string `envconfig:"API_KEY"`
// 	APISecretKey      string `envconfig:"API_SECRET_KEY"`
// 	AccesssToken      string `envconfig:"ACCESS_TOKEN"`
// 	AccessTokenSecret string `envconfig:"ACCESS_TOKEN_SECRET"`
// }

// var rep *regexp.Regexp = regexp.MustCompile("(@[A-Za-z0-9_]+\\s)|(https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+)|(`[\\s\\S]*?`)|(\n|\r\n|\r)")

// func deleteAutomaticTweet(text string) string {
// 	if strings.HasSuffix(text, "#contributter_report") ||
// 		strings.HasPrefix(text, "Liked on YouTube:") ||
// 		strings.Contains(text, "のポスト数") {
// 		text = ""
// 	}

// 	return text
// }

// func cleansingTweet(text string) string {
// 	text = deleteAutomaticTweet(text)
// 	text = rep.ReplaceAllString(text, "")
// 	text = html.UnescapeString(text)
// 	text = strings.TrimSpace(text)
// 	return text
// }

// func main() {
// 	var s specification
// 	err := envconfig.Process("", &s)
// 	if err != nil {
// 		log.Fatal(err.Error())
// 	}
// 	format := "API_KEY: %s\nAPI_SECRET_KEY: %s\nACCESS_TOKEN: %s\nACCESS_TOKEN_SECRET: %s\n"
// 	_, err = fmt.Printf(format, s.APIKey, s.APISecretKey, s.AccessTokenSecret, s.AccesssToken)
// 	if err != nil {
// 		log.Fatal(err.Error())
// 	}

// 	//  := anaconda.NewTwitterApiWithCredentials("your-access-token", "your-access-token-secret", "your-consumer-key", "your-consumer-secret")
// 	api := anaconda.NewTwitterApiWithCredentials(s.AccesssToken, s.AccessTokenSecret, s.APIKey, s.APISecretKey)

// 	var (
// 		res anaconda.SearchFullArchiveResponse
// 	)

// 	//os.O_RDWRを渡しているので、同時に読み込みも可能
// 	file, err := os.OpenFile("tweets-extra-7.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	defer file.Close()

// 	// fullArchiveAPIUrl := "https://api.twitter.com/1.1/tweets/search/fullarchive/ujimaru.json"
// 	query := "from:uzimaru0000"
// 	date := "202005170000"
// 	params := url.Values{
// 		"toDate": []string{date},
// 	}

// 	// fmt.Println(api.GetSearch("にじさんじ", nil))
// 	res, _ = api.GetSearchFrom30dayArchive(query, params, "ujimaru")
// 	fmt.Println("Next: ", res.Next)
// 	fmt.Println("Parameters: ", res.RequestParameters)
// 	fmt.Println("FromDate: ", res.RequestParameters.FromDate)
// 	fmt.Println("ToDate: ", res.RequestParameters.ToDate)
// 	fmt.Println("MaxResults: ", res.RequestParameters.MaxResults)
// 	for _, tweet := range res.Results {
// 		text := cleansingTweet(tweet.FullText)
// 		if text != "" {
// 			fmt.Fprintln(file, text)
// 		}
// 		fmt.Println(text)
// 		fmt.Println(tweet.CreatedAtTime())
// 	}
// 	time.Sleep(time.Second * 3)

// 	for i := 0; i < 100; i++ {
// 		params = url.Values{
// 			"toDate": []string{date},
// 			"next":   []string{res.Next},
// 		}

// 		res, _ = api.GetSearchFrom30dayArchive(query, params, "ujimaru")
// 		if len(res.Results) == 0 {
// 			break
// 		}

// 		for _, tweet := range res.Results {
// 			text := cleansingTweet(tweet.FullText)
// 			if text != "" {
// 				fmt.Fprintln(file, text)
// 			}
// 			fmt.Println(text)
// 			fmt.Println(tweet.CreatedAtTime())
// 		}

// 		time.Sleep(time.Second * 3)
// 	}

// }
