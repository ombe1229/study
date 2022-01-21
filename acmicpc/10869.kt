import java.util.*
import java.io.*

fun main() {
    val read = BufferedReader(InputStreamReader(System.`in`))
    val input = StringTokenizer(read.readLine())

    val a = input.nextToken().toInt()
    val b = input.nextToken().toInt()

    println(a + b)
    println(a - b)
    println(a * b)
    println(a / b)
    println(a % b)
}