package main

import (
	"fmt"
	"html"
	"log"
	"net/url"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/ChimeraCoder/anaconda"
	"github.com/kelseyhightower/envconfig"
)

type specification struct {
	APIKey            string `envconfig:"API_KEY"`
	APISecretKey      string `envconfig:"API_SECRET_KEY"`
	AccesssToken      string `envconfig:"ACCESS_TOKEN"`
	AccessTokenSecret string `envconfig:"ACCESS_TOKEN_SECRET"`
}

var rep *regexp.Regexp = regexp.MustCompile("(@[A-Za-z0-9_]+)|(https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+)|(`[\\s\\S]*?`)|(\n|\r\n|\r)")

func deleteAutomaticTweet(text string) string {
	if strings.Contains(text, "#contributter_report") ||
		strings.Contains(text, "#contributter") ||
		strings.Contains(text, "Liked on YouTube:") ||
		strings.Contains(text, "のポスト数") ||
		strings.Contains(text, "ポストに到達") ||
		strings.Contains(text, "RT @") ||
		strings.Contains(text, "#LAPRASポートフォリオ") ||
		strings.Contains(text, "#pixiv") {
		text = ""
	}

	return text
}

func cleansingTweet(text string) string {
	text = deleteAutomaticTweet(text)
	text = rep.ReplaceAllString(text, "")
	text = html.UnescapeString(text)
	text = strings.TrimSpace(text)
	return text
}

func main() {
	var s specification
	err := envconfig.Process("", &s)
	if err != nil {
		log.Fatal(err.Error())
	}
	format := "API_KEY: %s\nAPI_SECRET_KEY: %s\nACCESS_TOKEN: %s\nACCESS_TOKEN_SECRET: %s\n"
	_, err = fmt.Printf(format, s.APIKey, s.APISecretKey, s.AccessTokenSecret, s.AccesssToken)
	if err != nil {
		log.Fatal(err.Error())
	}

	//  := anaconda.NewTwitterApiWithCredentials("your-access-token", "your-access-token-secret", "your-consumer-key", "your-consumer-secret")
	api := anaconda.NewTwitterApiWithCredentials(s.AccesssToken, s.AccessTokenSecret, s.APIKey, s.APISecretKey)

	var (
		timeline []anaconda.Tweet
		query    url.Values
		maxID    string
	)

	userNames := []string{
		"uzimaru0000",
		"p1ass",
		"hpp_ricecake",
		"yt8492",
		"takanakahiko",
		"nasa_desu",
		"saitoeku3",
		"d0ra1998",
		"schktjm",
	}

	self, _ := api.GetSelf(query)
	fmt.Println("me", self.Name)

	time.Sleep(time.Second * 3)

	for _, userName := range userNames {
		maxID = ""
		fmt.Println("start:", userName)
		time.Sleep(time.Second * 3)
		//os.O_RDWRを渡しているので、同時に読み込みも可能
		file, err := os.OpenFile("tweets-"+userName+".txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		for {
			// get tweet id older than last tweet
			if len(timeline) != 0 {
				maxID = strconv.FormatInt(timeline[len(timeline)-1].Id-1, 10)
			}
			query = url.Values{
				"screen_name": []string{userName},
				"include_rts": []string{"false"},
			}
			if maxID != "" {
				query.Add("max_id", maxID)
			}

			timeline, _ = api.GetUserTimeline(query)
			if len(timeline) == 0 {
				break
			}

			for _, tweet := range timeline {
				text := cleansingTweet(tweet.FullText)
				if text != "" {
					fmt.Fprintln(file, text)
				}
				fmt.Println(text)
			}
			time.Sleep(time.Second * 3)
		}
	}
}
