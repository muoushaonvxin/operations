/**
 * Created by Selience on 2017/6/19.
 */
function Func(ths) {
    $(ths).next().removeClass('hide');
    $(ths).parent().siblings().find('.body').addClass('hide');
}