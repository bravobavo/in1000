1 = 1
2 = 0
4 = 0
8 = 1
16 = 1
10011 til binært

0 0 0 0 0 0 0 0 = bytes = 0
0 0 0 0 0 0 0 1 = bytes = 1
0 1 1 1 1 1 1 1 = 127 = 2⁷-1

2-er kompliment
Et negativ tall n lagres i 8 bit som 2⁸ + n = 256 + n
1 1 1 1 1 1 1 1 = -1 = 256-1
Omvendt, altså...
1 0 0 0 0 0 0 0 = -128 = -127 - 1


Java tilbyr disse tallene: byte(8), short(short), int(int), long (64bit)

class Overflyt {
    public static vodi main(String[arg]) {
        int v = 1000, v2 = v*v, v4 = v2*v

        System.out.printlin("v"+ v+ " og v2" + v2 + "og v4=" + v4)
    }
}
