use std::io::Read;
use curl::easy::Easy;

fn main() {
    let mut easy = Easy::new();

    // Headers
    list mut list = List::new();
    list.append("content-type: application/json").unwrap();
    list.append("")

    // Endpoint data
    let data = r#"
{ 'html': "<div class='box'>Hello, world!</div>",
'css': ".box { color: white; background-color: #0f79b9; padding: 10px; font-family: Roboto }",
'google_fonts': "Roboto" }"#;
    data = data.as_bytes();
    let HCTI_API_ENDPOINT = "https://hcti.io/v1/image";
    let HCTI_API_USER_ID = "dd0c7cce-2605-48e5-b0e5-a16269871f75";
    let HCTI_API_KEY = "e34a8eb4-c8f6-4a90-b51a-a63101079c4f";

    // image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY)

    easy.url("https://www.example.org/upload").unwrap();
    easy.post(true).unwrap();
    easy.post_field_size(data.len() as u64).unwrap();

    let mut transfer = easy.transfer();
    transfer.read_function(|buf| {
        Ok(data.read(buf)).unwrap_or(0)
    });
    transfer.perform().unwrap();
    
    println!("{}", easy.response_code().unwrap());
}
