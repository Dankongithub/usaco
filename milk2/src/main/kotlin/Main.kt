/*
ID: corbin.1
LANG: KOTLIN
TASK: milk2
 */


import java.io.File
import java.io.InputStream

fun minimumMaximum(inputList: Array<Int>): List<Int?> {
    val min = inputList.minOrNull()
    val max = inputList.maxOrNull()
    return listOf(min, max)
}



fun main() {
    val inputStream: InputStream = File("milk2.in").inputStream()
    val lineList = mutableListOf<String>()

    inputStream.bufferedReader().forEachLine { it ->
        val parts = it.trim().split(" ")
        parts.forEach {
            lineList.add(it)
        }
    }
    val N: String = lineList[0]
    println(N.toInt())
    lineList.removeAt(0)
    val minMax = minimumMaximum(lineList.map { it.toInt() }.toTypedArray())
    println(minMax)

    val min: Int? = minMax[0]
    val max: Int? = minMax[1]

    val listOfPairs = mutableListOf<Pair<Int, Int>>()
    for (i in 0 until N.toInt()) {
        listOfPairs.add(Pair(lineList[i*2].toInt(), lineList[i*2+1].toInt()))
    }
    println(listOfPairs)
    var longestTimeMilked = 0
    var longestTimeMilkedInInterval = 0
    var longestTimeNotMilked = 0
    var longestTimeNotMilkedInInterval = 0

    for (i in min!!..max!!) {
        var foundOrNot = false
        for (x in 0 until N.toInt()) {
            if (i >= listOfPairs[x].first && i < listOfPairs[x].second) {
                longestTimeMilkedInInterval += 1
                foundOrNot = true
                break
            }

        }


        if (longestTimeMilkedInInterval >= longestTimeMilked) {
            longestTimeMilked = longestTimeMilkedInInterval
        }
        if (!foundOrNot) {
            longestTimeMilkedInInterval = 0
            longestTimeNotMilkedInInterval += 1
            if (longestTimeMilkedInInterval >= longestTimeMilked) {
                longestTimeMilked = longestTimeMilkedInInterval
            }
        } else {
            if (longestTimeNotMilkedInInterval >= longestTimeNotMilked) {
                longestTimeNotMilked = longestTimeNotMilkedInInterval
            }
            longestTimeNotMilkedInInterval = 0



        }
    }
    println(longestTimeMilked)
    println(longestTimeNotMilked)
    File("milk2.out").writeText("$longestTimeMilked $longestTimeNotMilked \n")
}

