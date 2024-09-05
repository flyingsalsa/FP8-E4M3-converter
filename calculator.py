def fp8_e4m3_to_float(fp8):
    # Extract sign, exponent, and mantissa from 8 bits
    sign = (fp8 >> 7) & 0x1          # 1 bit for sign
    exponent = (fp8 >> 3) & 0xF       # 4 bits for exponent
    mantissa = fp8 & 0x7              # 3 bits for mantissa

    # Convert exponent (excess-7 bias)
    exponent_value = exponent - 7

    # Calculate mantissa value (implicit leading 1 for normalized numbers)
    if exponent != 0:  # Normalized
        mantissa_value = 1 + (mantissa / 8.0)  # 2^3 = 8, so mantissa / 8
    else:  # Denormalized (exponent = 0)
        mantissa_value = mantissa / 8.0  # No implicit leading 1 for subnormal numbers

    # Calculate the final floating-point value
    float_value = ((-1) ** sign) * (2 ** exponent_value) * mantissa_value
    print("Sign: {}, exponent: {}, mantissa: {}".format(sign,exponent,bin(mantissa)))
    return float_value

# Test examples (in binary)
test_values = [
    0b00101101,
    0b10110001,
    0xc3
]

# Print the floating-point values
for value in test_values:
    print(f"FP8: {bin(value)} -> Float: {fp8_e4m3_to_float(value)}")
