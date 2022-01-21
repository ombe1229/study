use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed");
    let parts: Vec<&str> = input.split_whitespace().collect();

    let a: i32 = parts[0].parse().unwrap();
    let b: i32 = parts[1].parse().unwrap();
    let c: i32 = parts[2].parse().unwrap();

    println!("{}", (a + b) % c);
    println!("{}", ((a % c) + (b % c)) % c);
    println!("{}", (a * b) % c);
    println!("{}", ((a % c) * (b % c)) % c);
}