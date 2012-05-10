require 'test/unit'
require_relative 'HW1'

class MyUnitTests < Test::Unit::TestCase

  def test_shout_with_number()
    assert_equal(shout(1), nil)
  end

  def test_shout_with_string()
    assert_equal(shout('I like Ruby.'), 'I LIKE RUBY!')
  end

  def test_reverse_with_string()
    assert_equal(reverse('Matt'), 'ttaM')
  end

  def test_reverse_words_with_string()
    x = "Matt likes to code."
    y = "code to likes Matt"
    assert_equal(reversewords(x), y)
  end

  def test_reverse_word_letters_with_string()
    x = "Matt likes to code."
    y = "ttaM sekil ot edoc"
    assert_equal(reversewordletters(x), y)
  end

  def reverse_letters_and_words()
    x = "Matt likes to code."
    y = "edoc ot sekil ttaM"
    reversewords(reversewordletters(x))
    assert_equal(z, y)
  end


end
