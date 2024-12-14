use std::{collections::HashSet, fs};

fn build_map(input: String) -> Vec<Vec<u32>> {
    input.split("\n")
        .map( 
            | line | 
            line.chars().map(
                |c| 
                c.to_digit(10).unwrap()
            ).collect()
        ).collect()
}

#[derive(Eq, Hash, PartialEq, Clone, Copy)]
struct Coord {
    i: usize,
    j: usize
}

fn calculate_paths(map: &Vec<Vec<u32>>, i: usize, j: usize, distinct_paths: bool) -> u32 {
    let mut visited: HashSet<Coord> = HashSet::new();
    let mut stack: Vec<Coord> = vec![Coord{i: i, j: j}];
    let mut path_sum = 0u32;
    while let Some(pos) = stack.pop() {
        if !distinct_paths {
            if visited.contains(&pos) {
                continue;
            }
            visited.insert(pos);
        }
        if map[pos.i][pos.j] == 9 {
            path_sum += 1;
        } else {
            let pos_height = map[pos.i][pos.j];
            if pos.i > 0 && map[pos.i - 1][pos.j] == pos_height + 1 {
                stack.push(Coord { i: pos.i - 1, j: pos.j});
            }
            if pos.i < map.len() - 1 && map[pos.i + 1][pos.j] == pos_height + 1 {
                stack.push(Coord { i: pos.i + 1, j: pos.j});
            }
            if pos.j > 0 && map[pos.i][pos.j - 1] == pos_height + 1 {
                stack.push(Coord { i: pos.i, j: pos.j - 1});
            }
            if pos.j < map[pos.i].len() - 1 && map[pos.i][pos.j + 1] == pos_height + 1 {
                stack.push(Coord { i: pos.i, j: pos.j + 1});
            }
        }
    }
    path_sum
}

fn task_1(map: Vec<Vec<u32>>) -> u32 {
    let mut path_sum: u32 = 0;
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if map[i][j] == 0 {
                path_sum += calculate_paths(&map, i, j, false);
            }
        }
    }
    return path_sum;
}

fn task_2(map: Vec<Vec<u32>>) -> u32 {
    let mut path_sum: u32 = 0;
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if map[i][j] == 0 {
                path_sum += calculate_paths(&map, i, j, true);
            }
        }
    }
    return path_sum;
}

fn main() {
    println!("There are {} start-peak combinations", task_1(build_map(fs::read_to_string("input.txt").unwrap())));
    println!("The rating sum of all hikes is {}", task_2(build_map(fs::read_to_string("input.txt").unwrap())));
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732";

    #[test]
    fn test_task_1() {
        let result = task_1(build_map(String::from(TEST_INPUT)));
        assert_eq!(result, 36);
    }

    #[test]
    fn test_task_2() {
        let result = task_2(build_map(String::from(TEST_INPUT)));
        assert_eq!(result, 81);
    }
}
