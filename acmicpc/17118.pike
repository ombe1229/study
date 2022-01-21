int main(){
    int a = (int)Stdio.stdin->gets();
    int ret = (860798509 * a + 198609463) % 1000000007;
    write((string)ret);
    return 0;
}