from os import system as s
print("Assembly (Bootloader):")
print("Executing NASM and QEMU...")
s("nasm -f bin hw.asm -o hw.bin && qemu-system-i386 -drive file=hw.bin,format=raw & > /dev/null")
print("C:")
s("gcc hw.c -o hw_c && ./hw_c")
print("C++:")
s("g++ hw.cpp -o hw_cpp && ./hw_cpp")
print("Dart:")
s("dart run hw.dart")
print("Elixir:")
s("elixir hw.ex")
print("Go:")
s("go run hw.go")
print("HTML:")
print("Executing Firefox...")
s("firefox hw.html & > /dev/null")
print("JS:")
s("node hw.js")
print("Pascal:")
s("fpc hw.pas -ohw_pas > /dev/null && ./hw_pas")
print("PHP:")
s("php hw.php")
print("Python:")
s("python3 hw.py")
print("Ruby:")
s("ruby hw.rb")
print("Rust:")
s("rustc hw.rs -o hw_rs && ./hw_rs")
print("Bash:")
s("sh hw.sh")
print("TS:")
s("ts-node hw.ts")
s("rm *_* *.bin *.o")
##Uncomment for cool screenshots.
#s("sleep 1000")
