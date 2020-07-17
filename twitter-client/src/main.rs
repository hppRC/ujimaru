use anyhow::Result;

async fn get_api_client() -> Result<kuon::TwitterAPI> {
    let access_token = &std::env::var("ACCESS_TOKEN")?;
    let access_token_secret = &std::env::var("ACCESS_TOKEN_SECRET")?;
    let api_key = &std::env::var("API_KEY")?;
    let api_secret_key = &std::env::var("API_SECRET_KEY")?;

    kuon::TwitterAPI::new(api_key, api_secret_key, access_token, access_token_secret).await
}

#[tokio::main]
async fn main() -> Result<()> {
    let api: kuon::TwitterAPI = get_api_client().await?;

    let endpoint = &std::env::var("UJIMARU_API")?;
    let text = reqwest::get(endpoint).await?.text().await?;

    let _ = api.tweet(&text).await;
    println!("{}", text);

    Ok(())
}
