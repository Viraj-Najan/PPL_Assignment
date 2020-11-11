void main() {
	__asm__("
			push   %rbp
			mov    %rsp,%rbp
			sub    $0x20,%rsp
			mov    %fs:0x28,%rax
			mov    %rax,-0x8(%rbp)
			xor    %eax,%eax
			lea    0x932fd(%rip),%rax        # 0x495004
			mov    %rax,-0x20(%rbp)
			movq   $0x0,-0x18(%rbp)
			mov    -0x20(%rbp),%rax
			lea    -0x20(%rbp),%rcx
			mov    $0x0,%edx
			mov    %rcx,%rsi
			mov    %rax,%rdi
			callq  0x447e60 <execve>
			nop
			mov    -0x8(%rbp),%rax
			xor    %fs:0x28,%rax
			je     0x401d40 <main+91>
			callq  0x44bc60 <__stack_chk_fail_local>
			leaveq
			retq
			.string \"/bin/sh\"
");
}

