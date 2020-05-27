
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

// 	// var (
// 	// 	timeline []anaconda.Tweet
// 	// 	query    url.Values
// 	// 	maxID    string
// 	// )

// 	//os.O_RDWRを渡しているので、同時に読み込みも可能
// 	file, err := os.OpenFile("tweets.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	defer file.Close()

// 	// fullArchiveAPIUrl := "https://api.twitter.com/1.1/tweets/search/fullarchive/ujimaru.json"
// 	query := "from:uzimaru0000"
// 	params := url.Values{}

// 	// fmt.Println(api.GetSearch("にじさんじ", nil))
// 	res, _ := api.GetSearchFromFullArchive(query, params, "ujimaru")
// 	fmt.Println("Next: ", res.Next)
// 	fmt.Println("Parameters: ", res.RequestParameters)
// 	fmt.Println("FromDate: ", res.RequestParameters.FromDate)
// 	fmt.Println("ToDate: ", res.RequestParameters.ToDate)
// 	fmt.Println("MaxResults: ", res.RequestParameters.MaxResults)

// 	for _, tweet := range res.Results {
// 		fmt.Println(tweet.FullText)
// 		fmt.Println(tweet.Id)
// 	}

// 	params = url.Values{
// 		"next": []string{res.Next},
// 	}
// 	res, _ = api.GetSearchFromFullArchive(query, params, "ujimaru")
// 	for _, tweet := range res.Results {
// 		fmt.Println(tweet.FullText)
// 		fmt.Println(tweet.Id)
// 	}
// }