import { createInterface } from "readline"

process.stdin.setEncoding('utf8');

let lines: string[] = [];

const rl = createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    main()
});

const follow = (users: string[][], log: number[]) => {
    const a = log[1]
    const b = log[2]

    // ユーザaがユーザbをフォローする。
    // すでにフォローしている場合は、何も起こらない。
    users[a-1][b-1] = "Y"
}

const allFollowBack = (users: string[][], log: number[]) => {
    const N = users.length
    const a = log[1]
    for (let i = 0; i < N; i++) {
        if (i === a-1) continue;

        if (users[i][a-1] === "Y") {
            users[a-1][i] = "Y";
        }
    }
}

// 問題点
const followFollow = (users: string[][], log: number[]) => {
    const N = users.length
    const a = log[1]


    // 現時点でユーザaをフォローしているユーザを取得
    let followers: number[] = []
    users[a-1].forEach((val, index) => {
        
        // console.log("val = "+ val + " : index = " + index)

        if (val === "Y") {
            followers.push(index)
        }
    })

    followers.forEach((num) => {
        users[num].forEach((val, index) => {
            if (index !== a-1 && val === "Y") {
                users[a-1][index] = "Y";
            }
        })
    })
}

const main = () => {
    // 隣接行列を作る
    const [N, Q] = lines[0].split(" ").map(Number);

    // 行・・・フォローするユーザー
    // 列・・・フォローされるユーザー
    let users = []
    for (let i = 0; i < N; i++) users.push(new Array(N).fill("N"))
    
    for (let i = 0; i < Q; i++) {
        const log = lines[1+i].split(" ").map(Number);

        switch (log[0]) {
            case 1:
                follow(users, log);
                break;
            case 2:
                allFollowBack(users, log)
                break;
            case 3:
                followFollow(users, log)
                break;
            default:
                // 入力エラーより、処理を中断
                return;
        }
    }

    users.forEach((ary) => {
        console.log(ary.join(""));
    })
}