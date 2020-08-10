const { once } = require('events')
const { createReadStream } = require('fs')
const { createInterface } = require('readline')

const startMap = new Map()
const finishMap = new Map()

async function processLineByLine() {
  try {
    const rl = createInterface({
      input: createReadStream('acslog-rchcnnapi-main-200731-200801.txt'),
      crlfDelay: Infinity
    })

    rl.on('line', (line) => {
      try {
        const obj = JSON.parse(line)
        const content = JSON.parse(obj.content)
        startMap.set(content.requestId, obj['__tag__:__hostname__'] + ', ' + new Date(Number(obj.__time__) * 1000).toISOString() + ', ' + content.url)
      } catch ( e ) {
        console.log('报错：跳过')
      }
    })
    await once(rl, 'close')

    console.log('文件 1 已处理')


    const rl2 = createInterface({
      input: createReadStream('acslog-rchcnnapi-main-200731-200801-2.txt'),
      crlfDelay: Infinity
    })

    rl2.on('line', (line) => {
      try {
        const obj = JSON.parse(line)
        const content = JSON.parse(obj.content)
        finishMap.set(content.requestId, content.url)
      } catch ( e ) {
        console.log('报错：跳过')
      }
    })
    await once(rl2, 'close')

    console.log('文件 2 已处理')

    const diffMap = new Map()

    startMap.forEach((value, key) => {
      if (!finishMap.has(key)) {
        diffMap.set(key, value)
      }
    })

    console.log('startMap = ' + startMap.size)
    console.log('finishMap = ' + finishMap.size)
    console.log('没有 finiish 的请求数' + diffMap.size)
    diffMap.forEach((value, key) => console.log(key + ', ' + value))

  } catch ( err ) {
    console.error(err)
  }
}

processLineByLine()
