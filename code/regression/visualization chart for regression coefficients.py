import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def create_regression_coefficient_plot(data, categories, bg_colors, label_colors,
                                       positive_color='orange', negative_color='blue',
                                       colla_work_count_color='gray', figsize=(18, 6)):
    """
    Generate a comparative visualization chart for regression coefficients across multiple fields

    Parameters:
    - data: Dictionary containing regression coefficients and significance for each field
    - categories: List of all category names
    - bg_colors: Dictionary mapping each category to its background color
    - label_colors: Dictionary mapping each category to its label color
    - positive_color: Color for data points with positive coefficients
    - negative_color: Color for data points with negative coefficients
    - colla_work_count_color: Color for the data points of "colla_work_count"
    - figsize: Tuple specifying figure size (width, height)
    """
    # Create a subplot layout with one row and multiple columns
    fig, axes = plt.subplots(1, len(data), figsize=figsize, sharey=True)

    # Ensure axes is an array, handle single field case
    if len(data) == 1:
        axes = [axes]

    # Plot each field's data in its respective subplot
    for i, (field, field_data) in enumerate(data.items()):
        ax = axes[i]
        coefficients = field_data['coefficients']
        significance = field_data['significance']

        # Plot background rectangles and data points
        for j, category in enumerate(categories):
            # Set data point color: default based on coefficient sign, special category uses neutral color
            point_color = colla_work_count_color if category == 'colla_work_count' else (
                positive_color if coefficients[j] >= 0 else negative_color
            )

            # Add background rectangle
            ax.add_patch(Rectangle(xy=(-1.5, j - 0.5), width=3, height=1,
                                   color=bg_colors[category], alpha=0.8))

            # Plot data point
            ax.plot(coefficients[j], j, 'o', color=point_color, markersize=11)

            # Adjust alignment of significance markers based on point color
            h_align = 'left' if point_color in [negative_color, colla_work_count_color] else 'right'
            offset = 0.1 if h_align == 'left' else -0.1

            # Add significance marker text
            ax.text(coefficients[j] + offset, j, significance[j],
                    verticalalignment='center', horizontalalignment=h_align,
                    color='black', fontsize=16)

        # Setup plot style
        _setup_plot_style(ax, field, categories, label_colors, len(data) > 1 and i == 0)

    # Adjust subplot spacing and return figure object
    plt.subplots_adjust(wspace=0.1)
    plt.tight_layout()
    return fig, axes


def _setup_plot_style(ax, title, categories, label_colors, is_first_ax):
    """Setup style for an individual subplot"""
    # Add reference line and grid
    ax.axvline(x=0, color='black', linestyle='--', alpha=0.7)
    ax.grid(axis='y', linestyle='--', color='gray', linewidth=1)
    ax.grid(axis='x', linestyle='--', color='gray', linewidth=1)

    # Set axes and title
    ax.set_xlabel('Coefficient estimate', fontsize=18)
    ax.set_title(title, fontsize=23, fontweight='bold')
    ax.set_xlim(-1.5, 1.5)
    ax.tick_params(axis='x', labelsize=16)

    # Set y-axis labels (only on the first subplot)
    if is_first_ax:
        yticks = np.arange(len(categories))
        ax.set_yticks(yticks)
        ax.set_yticklabels(categories, fontsize=16)
        for tick, category in zip(ax.get_yticklabels(), categories):
            tick.set_color(label_colors[category])

    # Set spine styles
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2.0)
    ax.spines['bottom'].set_linewidth(2.0)


def main():
    """Main function: configure data and generate chart"""
    # Define variables and color configurations
    categories = ['ave_distance', 'ave_distance²', 'career_len_mte', 'mte_work_count_first_5y',
                  'topic_num_mto', 'total_cits_mto', 'colla_work_count', 'colla_work_count_first_5y',
                  'colla_work_count_later', 'common_collaborators_count']

    # Background color configuration
    bg_colors = {
        'ave_distance': '#EFEFEF', 'ave_distance²': '#EFEFEF',
        'career_len_mte': '#EEEAEA', 'mte_work_count_first_5y': '#EEEAEA',
        'topic_num_mto': '#E7F3F7', 'total_cits_mto': '#E7F3F7',
        'colla_work_count': '#DFF9DD', 'colla_work_count_first_5y': '#DFF9DD',
        'colla_work_count_later': '#DFF9DD', 'common_collaborators_count': '#DFF9DD'
    }

    # Y-tick label color configuration
    label_colors = {
        'ave_distance': '#404040', 'ave_distance²': '#404040',
        'career_len_mte': '#B71C1C', 'mte_work_count_first_5y': '#B71C1C',
        'topic_num_mto': '#01579B', 'total_cits_mto': '#01579B',
        'colla_work_count': '#2E7D32', 'colla_work_count_first_5y': '#2E7D32',
        'colla_work_count_later': '#2E7D32', 'common_collaborators_count': '#2E7D32',
    }

    # Data point color configuration
    neutral_color = 'gray'
    positive_color = 'orange'
    negative_color = 'blue'

    # Data for three fields
    data = {
        'Chemistry': {
            'coefficients': [0.448, -0.048, 1.303, 0.559, -1.219, 0.390, -0.004, -0.026, -0.190, 0.353],
            'significance': ['***', '***', '***', '***', '***', '***', '', '', '***', '***']
        },
        'Neuroscience': {
            'coefficients': [0.250, -0.044, 0.557, 0.629, -1.458, 0.345, -0.058, -0.028, -0.307, 0.422],
            'significance': ['***', '***', '***', '***', '***', '***', '***', '', '***', '***']
        },
        'Physics': {
            'coefficients': [0.897, -0.094, 0.560, 0.651, -1.147, 0.478, 0.035, -0.150, 0.038, 0.081],
            'significance': ['***', '***', '***', '***', '***', '***', '', '***', '', '**']
        }
    }

    # Create chart
    fig, axes = create_regression_coefficient_plot(
        data, categories, bg_colors, label_colors,
        positive_color, negative_color, neutral_color
    )

    # Save and display chart
    plt.savefig('regression_coefficients.pdf', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()