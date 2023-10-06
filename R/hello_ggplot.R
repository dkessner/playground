#!/usr/bin/env Rscript

library(tidyverse)
library(palmerpenguins)
library(ggthemes)

ggplot(data = penguins,
       mapping = aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color = species, shape = species)) +
  geom_smooth(method = "lm") +
  labs(
    title = "Body mass and flipper length",
    subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
    x = "Flipper length (mm)", y = "Body mass (g)",
    color = "Species", shape = "Species"
  ) +
  scale_color_colorblind()

ggsave(filename = "penguin-plot.png")


# pipe notation

penguins |> 
  ggplot(aes(x = flipper_length_mm, y = body_mass_g)) + 
  geom_point()

ggsave(filename = "penguin-plot-2.png")


# automatically writes Rplots.pdf with both plots?

