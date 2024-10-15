import readline from "readline"

process.stdin.setEncoding('utf8')

let lines: string[] = []
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (line) => {
    lines.push(line)
})

rl.on("close", () => {
    main()
})

const main = () => {
    const [N, M] = lines[0].split(" ").map(Number)
    const A: number[] = lines[1].split(" ").map(Number)

    type NumDictionary = {
        [key: number]: number
    }

    let count: NumDictionary = {}

    // O(N)
    for (let i = 0; i < N; i++) {
        // オブジェクトの
        if (!(A[i] in count)) {
            count[A[i]] = 0
        }
        count[A[i]] += 1
    }

    // O(M)
    for (let i = 0; i < M; i++) {
        if (!(A[i] in count)) {
            console.log(0)
        } else {
            console.log(count[A[i]])
        }
    }

    // 計算回数 O(N+M)
} 