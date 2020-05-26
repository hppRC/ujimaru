package main

import (
	"fmt"
	"log"

	"github.com/ChimeraCoder/anaconda"
	"github.com/kelseyhightower/envconfig"
)

type Specification struct {
	APIKey            string `envconfig:"API_KEY"`
	APISecretKey      string `envconfig:"API_SECRET_KEY"`
	AccesssToken      string `envconfig:"ACCESS_TOKEN"`
	AccessTokenSecret string `envconfig:"ACCESS_TOKEN_SECRET"`
}

func main() {
	var s Specification
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

	searchResult, _ := api.GetSearch("にじさんじ", nil)
	for _, tweet := range searchResult.Statuses {
		api.Favorite(tweet.Id)
	}
}
