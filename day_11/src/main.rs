use regex::Regex;
use std::{
    collections::HashMap,
    fs,
    str::FromStr,
    thread::{self},
};

fn split_input(input: &str) -> Vec<u64> {
    let re = Regex::new(r"(\d+)").unwrap();
    re.find_iter(input)
        .filter_map(|m| FromStr::from_str(m.as_str()).ok())
        .collect()
}

fn task_1(mut stones: Vec<u64>, blinks: u32) -> usize {
    println!("{:?}", stones);
    for blink in 0..blinks {
        println!("Blink {}", blink);
        let mut i: usize = 0;
        while i < stones.len() {
            if stones[i] == 0 {
                stones[i] = 1;
            } else if stones[i].to_string().len() % 2 == 0 {
                let stone = stones[i].to_string();
                let (a, b) = stone.split_at(stone.len() / 2);
                stones[i] = FromStr::from_str(a).unwrap();
                stones.insert(i + 1, FromStr::from_str(b).unwrap());
                i += 1;
            } else {
                stones[i] *= 2024;
            }
            i += 1;
        }
    }
    stones.len()
}

fn blink(stones: Vec<u64>, blinks: u32) -> Vec<(u32, u64)> {
    let mut stack: Vec<(u32, u64)> = stones.iter().map(|stone| (0u32, *stone)).collect();
    let mut result: Vec<u64> = vec![];
    while let Some((blink, num)) = stack.pop() {
        if blink == blinks {
            result.push(num);
        } else if num == 0 {
            stack.push((blink + 1, 1u64));
        } else if num.ilog10() % 2 == 1 {
            let exp = (num.ilog10() / 2) + 1;
            let splitter = 10u64.pow(exp);
            let left = num / splitter;
            let right = num % splitter;
            stack.push((blink + 1, right));
            stack.push((blink + 1, left));
        } else {
            stack.push((blink + 1, num * 2024));
        }
    }
    return result.into_iter().map(|num| (blinks, num)).collect();
}

fn task_2(stones: Vec<u64>, blinks: u32) -> u64 {
    let mut stack: Vec<(u32, u64)> = stones.iter().map(|stone| (0u32, *stone)).collect();
    let mut stone_count: u64 = 0;
    while let Some((blink, num)) = stack.pop() {
        if blink == blinks {
            stone_count += 1;
        } else if num == 0 {
            stack.push((blink + 1, 1u64));
        } else if num.ilog10() % 2 == 1 {
            let exp = (num.ilog10() / 2) + 1;
            let splitter = 10u64.pow(exp);
            let left = num / splitter;
            let right = num % splitter;
            stack.push((blink + 1, right));
            stack.push((blink + 1, left));
        } else {
            stack.push((blink + 1, num * 2024));
        }
    }
    return stone_count;
}

fn task_2_map(stones: Vec<u64>, blinks: u32) -> u64 {
    let mut map1: HashMap<u64, u64> = HashMap::new();
    let mut map2: HashMap<u64, u64> = HashMap::new();
    // fill first hashmap
    for stone in stones {
        *map1.entry(stone).or_insert(0) += 1;
    }
    for blink in 1..blinks + 1 {
        // println!("Blink {blink}");
        for stone in map1.keys() {
            if *stone == 0 {
                *map2.entry(1).or_insert(0) += map1[stone];
            } else if stone.ilog10() % 2 == 1 {
                let exp = (stone.ilog10() / 2) + 1;
                let splitter = 10u64.pow(exp);
                let left = stone / splitter;
                let right = stone % splitter;
                *map2.entry(left).or_insert(0) += map1[stone];
                *map2.entry(right).or_insert(0) += map1[stone];
            } else {
                *map2.entry(stone * 2024).or_insert(0) += map1[stone];
            }
        }

        map1 = map2.clone();
        map2.clear();
    }
    map1.values().sum()
}

fn thread_splitting(stones: Vec<u64>, blinks: u32, threads: usize) -> u64 {
    let mut stone_count: u64 = 0;
    let mut splitted: Vec<Vec<u64>> = vec![];
    let mut thread: usize = 0;
    for val in stones {
        if thread >= splitted.len() {
            splitted.push(vec![]);
        }
        splitted[thread].push(val);
        thread = (thread + 1) % threads;
    }
    println!("{:?}", splitted);
    let mut thread_handles = vec![];
    for split in splitted {
        thread_handles.push(thread::spawn(move || task_2(split, blinks)));
    }

    for th in thread_handles {
        stone_count += th.join().unwrap();
    }
    return stone_count;
}

fn main() {
    println!(
        "After 25 blinks, there are {} stones",
        task_2(
            split_input(fs::read_to_string("input.txt").unwrap().as_str()),
            25
        )
    );
    // part 2 is the same but with more blinks... lets hope this don't fill the memory
    /*
        println!(
            "After 75 blinks, there are {} stones",
            task_2(
                split_input(fs::read_to_string("input.txt").unwrap().as_str()),
                75
            )
    );
        */
    /*
    println!(
        "After 75 blinks, there are {} stones",
        thread_splitting(
            split_input(fs::read_to_string("input.txt").unwrap().as_str()),
            50
        )
    );
     */
    println!(
        "After 75 blinks, there are {} stones",
        task_2_map(
            split_input(fs::read_to_string("input.txt").unwrap().as_str()),
            75
        )
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "125 17";

    #[test]
    fn test_1() {
        assert_eq!(55312, task_1(split_input(TEST_INPUT), 25));
    }

    #[test]
    fn test_2() {
        assert_eq!(55312, task_2(split_input(TEST_INPUT), 25));
    }

    #[test]
    fn test_2_threaded() {
        assert_eq!(55312, thread_splitting(split_input(TEST_INPUT), 25, 6));
    }

    #[test]
    fn test_2_map() {
        assert_eq!(55312, task_2_map(split_input(TEST_INPUT), 25));
    }
}
