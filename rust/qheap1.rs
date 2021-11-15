use std::io::{self, Write};
use std::vec::Vec;


fn get_input() -> String {
    let mut input: String = String::new();
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line.");
    return input.trim().to_string();
}


fn main() {
    let q: i32 = get_input().parse::<i32>().unwrap();
    let mut heap: Vec<i32> =  Vec::new();

    for _ in 0 .. q {
        let input = get_input();
        let query = input.split(" ").collect::<Vec<&str>>();

        if query[0] == "1" { // Add element query[1] to Heap
            heap.push(query[1].parse::<i32>().unwrap());
        } else if query[0] == "2" { // Remove element query[1] from Heap
            let finding: i32 = query[1].parse::<i32>().unwrap();
            heap.remove(heap.iter().position(|x| *x == finding).unwrap());
        } else if query[0] == "3" { // Print minimum element of Heap
            println!("{}", heap.iter().min().unwrap());
        }
    }
}