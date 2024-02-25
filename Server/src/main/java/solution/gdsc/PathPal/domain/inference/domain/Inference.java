package solution.gdsc.PathPal.domain.inference.domain;

public record Inference(String name, double confidence,
                        double left_x, double right_x,
                        double up_y, double down_y,
                        boolean alert) {
}

