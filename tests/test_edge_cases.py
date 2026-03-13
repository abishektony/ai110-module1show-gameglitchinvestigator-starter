import pytest
from logic_utils import parse_guess, check_guess


class TestEdgeCases:
    """Test edge cases that could break the number guessing game."""

    # ===== EDGE CASE 1: Extremely Large Numbers =====
    class TestExtremelyLargeNumbers:
        """Test behavior with extremely large numeric inputs."""

        def test_very_large_positive_number(self):
            """Test input with 10+ digit number."""
            ok, guess_int, err = parse_guess("999999999999")
            assert ok is True
            assert guess_int == 999999999999
            assert err is None

        def test_scientific_notation_large(self):
            """Test scientific notation for large numbers (1e10 = 10,000,000,000)."""
            ok, guess_int, err = parse_guess("1e10")
            # EDGE CASE BUG: "1e10" has no ".", so code tries int("1e10") which fails
            # Should ideally parse scientific notation, but doesn't
            assert ok is False
            assert err is not None
            assert "number" in err.lower()

        def test_large_number_breaks_range_check(self):
            """Test that game doesn't validate if guess is within difficulty range."""
            # Easy mode range is 1-20, but we can guess 999
            ok, guess_int, err = parse_guess("999")
            assert ok is True
            assert guess_int == 999
            # Game should ideally reject this, but currently doesn't


    # ===== EDGE CASE 2: Negative Numbers =====
    class TestNegativeNumbers:
        """Test behavior with negative numeric inputs."""

        def test_negative_number_accepted(self):
            """Test that negative numbers are accepted by parser."""
            ok, guess_int, err = parse_guess("-50")
            assert ok is True
            assert guess_int == -50
            assert err is None

        def test_negative_float_accepted(self):
            """Test that negative floats are accepted and converted to int."""
            ok, guess_int, err = parse_guess("-25.7")
            assert ok is True
            assert guess_int == -25
            assert err is None

        def test_very_large_negative_number(self):
            """Test extremely large negative number."""
            ok, guess_int, err = parse_guess("-9999999999")
            assert ok is True
            assert guess_int == -9999999999
            assert err is None

        def test_negative_guess_vs_positive_secret(self):
            """Test comparison of negative guess against positive secret."""
            outcome, message = check_guess(-5, 50)
            # Negative is always less than positive, so "Too Low"
            assert outcome == "Too Low"
            assert "HIGHER" in message


    # ===== EDGE CASE 3: Floating Point Edge Cases =====
    class TestFloatingPointEdgeCases:
        """Test behavior with special floating point values."""

        def test_decimal_with_many_places(self):
            """Test float with many decimal places."""
            ok, guess_int, err = parse_guess("42.999999999999")
            assert ok is True
            assert guess_int == 42
            assert err is None

        def test_very_small_decimal(self):
            """Test very small decimal that rounds to 0."""
            ok, guess_int, err = parse_guess("0.00001")
            assert ok is True
            assert guess_int == 0
            assert err is None

        def test_infinity_string(self):
            """Test if 'inf' is handled (should fail or convert)."""
            ok, guess_int, err = parse_guess("inf")
            # This should fail because float('inf') can't convert to int
            assert ok is False
            assert err is not None
            assert "number" in err.lower()

        def test_nan_string(self):
            """Test if 'nan' is handled (should fail or convert)."""
            ok, guess_int, err = parse_guess("nan")
            # This should fail because float('nan') can't convert to int
            assert ok is False
            assert err is not None
            assert "number" in err.lower()

        def test_zero_guess(self):
            """Test edge case of guessing 0."""
            ok, guess_int, err = parse_guess("0")
            assert ok is True
            assert guess_int == 0
            # 0 is outside normal range (1-20, 1-50, 1-100) but parser accepts it

        def test_float_string_with_leading_zero(self):
            """Test float string like '007.5'."""
            ok, guess_int, err = parse_guess("007.5")
            assert ok is True
            assert guess_int == 7
            assert err is None


class TestEdgeCaseGameLogic:
    """Test how edge cases interact with game comparison logic."""

    def test_negative_vs_negative_comparison(self):
        """Test comparing two negative numbers."""
        outcome, message = check_guess(-10, -20)
        # -10 > -20, so "Too High"
        assert outcome == "Too High"

    def test_zero_vs_positive_comparison(self):
        """Test comparing zero to positive secret."""
        outcome, message = check_guess(0, 50)
        assert outcome == "Too Low"

    def test_string_secret_with_large_number(self):
        """Test the string comparison bug with large numbers."""
        # When attempts % 2 == 0, secret becomes a string
        # This tests string vs int comparison with TypeError fallback
        outcome, message = check_guess(100, "50")
        # EDGE CASE BUG: int > str raises TypeError → except block does string comparison
        # "100" > "50" is False (lexicographically '1' < '5'), so returns "Too Low"
        # This is wrong! 100 should be > 50 as numbers
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_string_secret_single_vs_multi_digit(self):
        """Test string comparison between single and multi-digit numbers."""
        outcome, message = check_guess(9, "100")
        # String comparison: "9" > "100" lexicographically (because '9' > '1')
        assert outcome == "Too High"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
