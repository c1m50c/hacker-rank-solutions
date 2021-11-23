use std::io::{self, Write};


fn input() -> String {
    let mut input: String = String::new();
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line.");
    return input.trim().to_string();
}


fn solve() {

}


fn main() {
    solve();
}